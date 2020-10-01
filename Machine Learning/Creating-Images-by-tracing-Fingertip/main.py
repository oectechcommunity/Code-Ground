from cv2 import cv2
import numpy as np
import math
import time

import color_palette


bg = None

image_weight = 0.5

top, bottom, left, right = 20, 450, 320, 620

palette_left = left + 60
palette_top = bottom - 70

number_of_frames = 0

fingertip_current_trace = np.ones(shape=[300, 300, 3], dtype=np.uint8)
fingertip_current_trace = fingertip_current_trace*255
fingertip_prev_trace = fingertip_current_trace
prevPoint = None

color_blue      = (255, 0, 0)
color_green     = (0, 255, 0)
color_red       = (0, 0, 255)
color_yellow    = (0, 255, 255)
color_orange    = (0, 165, 255)
color_magenta   = (255, 0, 255)
color_black     = (0, 0, 0)
color_cyan      = (255, 255, 0)
color_brown     = (19, 69, 139)
color_white     = (255, 255, 255)
color_purple    = (153, 0, 153)
color_olive     = (0, 128, 128)

picked_color = color_green
prev_color = None
wait_time_counter = 0

euclidean_dist_threshold = 10
number_of_frames_threshold = 40



def preprocess_frame(camera):
    (ret_value, frame) = camera.read()

    frame = cv2.flip(frame, 1)

    clone = frame.copy()

    cv2.rectangle(clone, (left, top), (right, bottom-130), color_green, 3)

    cv2.putText(clone, 'Draw in the above area', (left, bottom - 110), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color_green, thickness=2)
    cv2.putText(clone, 'Color palette', (palette_left, bottom - 80), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color_green, thickness=2)

    region_of_trace = frame[top:bottom, left:right]

    gray = cv2.cvtColor(region_of_trace, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    return clone, region_of_trace, gray


def create_color_palette(image, color, palette_point):
    color_palette_obj = color_palette.ColorPalette(image, color, palette_point)
    color_palette_obj.create_color_palette()


def run_avg(image):
    global bg
    global image_weight

    if bg is None:
        bg = image.copy().astype("float")
        return
    cv2.accumulateWeighted(image, bg, image_weight)


def segment(image):
    global bg
    global number_of_frames_threshold

    diff = cv2.absdiff(bg.astype("uint8"), image)
    threshold_image = cv2.threshold(diff, number_of_frames_threshold, 255, cv2.THRESH_BINARY)[1]
    contours, hierarchy = cv2.findContours(threshold_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return
    else:
        segmented_image = max(contours, key=cv2.contourArea)
        return (threshold_image, segmented_image)


def convexhull(segmented_image):
    convexHull = cv2.convexHull(segmented_image)
    return convexHull


def determine_current_color(x, y):
    if y in range(palette_top, palette_top + 30):
        if x in range(palette_left, palette_left + 30):
            color = color_blue
        elif x in range(palette_left + 30, palette_left + 60):
            color = color_green
        elif x in range(palette_left + 60, palette_left + 90):
            color = color_red
        elif x in range(palette_left + 90, palette_left + 120):
            color = color_yellow
        elif x in range(palette_left + 120, palette_left + 150):
            color = color_orange
        elif x in range(palette_left + 150, palette_left + 180):
            color = color_magenta

    if y in range(palette_top + 30, palette_top + 60):
        if x in range(palette_left, palette_left + 30):
            color = color_black
        elif x in range(palette_left + 30, palette_left + 60):
            color = color_cyan
        elif x in range(palette_left + 60, palette_left + 90):
            color = color_brown
        elif x in range(palette_left + 90, palette_left + 120):
            color = color_white
        elif x in range(palette_left + 120, palette_left + 150):
            color = color_purple
        elif x in range(palette_left + 150, palette_left + 180):
            color = color_olive

    return color


def close_vdo_download_img(fingertip_current_trace):
    file_name = "Trace_Image_" + time.strftime('%Y%m%d%H%M%S') + ".jpg"

    camera.release()
    cv2.destroyAllWindows()

    cv2.imwrite(file_name, fingertip_current_trace)
    print("Image saved successfully!!!")



def main():
    global image_weight
    global top, bottom, left, right
    global number_of_frames
    global prevPoint, fingertip_current_trace, fingertip_prev_trace
    global picked_color, prev_color, wait_time_counter
    global euclidean_dist_threshold, number_of_frames_threshold

    while (True):

        clone, region_of_trace, gray = preprocess_frame(camera)

        create_color_palette(clone, color_blue, (palette_left, palette_top))
        create_color_palette(clone, color_green, (palette_left+30, palette_top))
        create_color_palette(clone, color_red, (palette_left+60, palette_top))
        create_color_palette(clone, color_yellow, (palette_left+90, palette_top))
        create_color_palette(clone, color_orange, (palette_left+120, palette_top))
        create_color_palette(clone, color_magenta, (palette_left+150, palette_top))

        create_color_palette(clone, color_black, (palette_left, palette_top+30))
        create_color_palette(clone, color_cyan, (palette_left+30, palette_top+30))
        create_color_palette(clone, color_brown, (palette_left+60, palette_top+30))
        create_color_palette(clone, color_white, (palette_left+90, palette_top+30))
        create_color_palette(clone, color_purple, (palette_left+120, palette_top+30))
        create_color_palette(clone, color_olive, (palette_left+150, palette_top+30))

        keypress = cv2.waitKey(1) & 0xFF

        if number_of_frames < number_of_frames_threshold:
            run_avg(gray)
        else:
            hand = segment(gray)

            if hand is not None:

                (threshold_image, segmented_image) = hand

                convexHull = convexhull(segmented_image)
                convexHull_top_point = tuple(convexHull[convexHull[:, :, 1].argmin()][0])

                convexHull_top_point_clone_x = convexHull_top_point[0]+left
                convexHull_top_point_clone_y = convexHull_top_point[1]+top
                convexHull_top_point_clone   = (convexHull_top_point_clone_x, convexHull_top_point_clone_y)

                if (convexHull_top_point_clone_x in range(palette_left, palette_left+180) and
                    (convexHull_top_point_clone_y in range(palette_top, palette_top+60))):

                    color = determine_current_color(convexHull_top_point_clone_x, convexHull_top_point_clone_y)

                    if color == prev_color:
                        wait_time_counter += 1
                        if wait_time_counter >= 50:
                            picked_color = color
                    elif color != prev_color:
                        wait_time_counter = 0

                    prev_color = color

                cv2.circle(clone, convexHull_top_point_clone, radius=1, color=picked_color, thickness=2)

                if prevPoint is None:
                    cv2.circle(fingertip_current_trace, convexHull_top_point, radius=1, color=picked_color,
                                                 thickness=2)

                    prevPoint = convexHull_top_point
                    fingertip_prev_trace = fingertip_current_trace

                else:
                    euclidean_dist = int(abs(math.sqrt(
                        (prevPoint[0] - convexHull_top_point[0]) ** 2 + (prevPoint[1] - convexHull_top_point[1]) ** 2)))

                    if euclidean_dist <= euclidean_dist_threshold:
                        cv2.line(fingertip_current_trace, prevPoint, convexHull_top_point, color=picked_color,
                                                   thickness=2)
                        cv2.imshow("White Board", fingertip_current_trace)

                    else:
                        cv2.circle(fingertip_prev_trace, convexHull_top_point, radius=1, color=picked_color,
                                                     thickness=2)
                        cv2.imshow("White Board", fingertip_prev_trace)

                        prevPoint = convexHull_top_point
                        fingertip_prev_trace = cv2.addWeighted(fingertip_current_trace, 1.0, fingertip_prev_trace, 0.0, 0)

                        cv2.imshow("Video Stream", clone)
                        number_of_frames += 1

                        if keypress == 27:
                            break

                        continue

        cv2.imshow("Video Stream", clone)
        number_of_frames += 1

        if keypress == 27:
            break

if __name__ == "__main__":
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    main()
    close_vdo_download_img(fingertip_current_trace)