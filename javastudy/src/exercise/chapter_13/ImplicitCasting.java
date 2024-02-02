package exercise.chapter_13;

public class ImplicitCasting {

    public static void main(String[] args) {
//        //덜 정밀한 자료형 -> 더 정밀한 자료형
//        int myInt = 5;
//        float myFloat = myInt;
//        System.out.println(myFloat); //5.0

        //사이즈가 작은 타입 -> 사이즈가 큰 타입
        int myInt = 10;
        long myLong = myInt;
        System.out.println(myLong); //10
    }
}
