package exercise.chapter_21;

import java.lang.reflect.Array;
import java.util.Arrays;

public class ArrayCopy {
    public static void main(String[] args) {

        //리터럴 깊은 복사
        int a = 5;
        int b = a;

        b+=5;

        System.out.println(a); //5
        System.out.println(b); //10

        //array 얇은 복사
        int[] arr1 = {1,2,3,4};
        int[] arr2 = arr1;

        arr1[0] = 10;

        System.out.println(Arrays.toString(arr1)); //[10, 2, 3, 4]
        System.out.println(Arrays.toString(arr2)); //[10, 2, 3, 4]
    }
}
