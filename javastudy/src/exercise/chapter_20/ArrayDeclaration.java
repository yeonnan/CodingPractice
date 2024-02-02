package exercise.chapter_20;

import java.util.Arrays;

public class ArrayDeclaration {
    public static void main(String[] args) {

        //int[]
        int[] intArr = new int[10];
        int[] intArr2 = new int[]{1,2,3,4,5}; //선언과 동시에 어떤 값이 들어갈지 정의
        int[] intArr3 = {1,2,3,4,5};

        System.out.println(Arrays.toString(intArr)); //[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        System.out.println(Arrays.toString(intArr2)); //[1, 2, 3, 4, 5]
        System.out.println(Arrays.toString(intArr3)); //[1, 2, 3, 4, 5]

        //float[]
        float[] floatArr = new float[10];
        float[] floatArr2 = {1.5f, 2.5f, 3.5f};

        System.out.println(Arrays.toString(floatArr)); //[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        System.out.println(Arrays.toString(floatArr2)); //[1.5, 2.5, 3.5]

        //boolean
        boolean[] booleans = new boolean[5];
        boolean[] booleans2 = {true, false, true};

        System.out.println(Arrays.toString(booleans)); //[false, false, false, false, false]
        System.out.println(Arrays.toString(booleans2)); //[true, false, true]

        //char String
        char[] charArr = new char[10];
        char[] charArr2 = {'A', 'B', 'C'};
        String[] stringArr = new String[10];
        String[] stringArr2 = {"ABC", "Hello", "World"};

        System.out.println(Arrays.toString(charArr)); //[ ,  ,  ,  ,  ,  ,  ,  ,  ,  ]
        System.out.println(Arrays.toString(charArr2)); //[A, B, C]
        System.out.println(Arrays.toString(stringArr)); //[null, null, null, null, null, null, null, null, null, null]
        System.out.println(Arrays.toString(stringArr2)); //[ABC, Hello, World]

    }
}
