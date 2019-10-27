    #include<stdio.h>
    #include<math.h>
     
    main()
    {
       float radius, area;
       
       printf("Enter the radius of circle\n");
       
       scanf("%f",&radius);
       
       /* M_PI (pi) is a constant in math.h header file */
     
       area = M_PI*radius*radius;  
       
       printf("Area of circle = %.2f\n", area);
       
       return 0;
    }
