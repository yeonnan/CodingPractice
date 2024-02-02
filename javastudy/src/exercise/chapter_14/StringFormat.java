package exercise.chapter_14;

public class StringFormat {

    public static void main (String[]args) {

        //String 생성방식
        String str1 = "Happy";
        String str2 = String.valueOf(123);

        System.out.println(str1);
        System.out.println(str2);

        //String 1 기존스트링을 다른 스트링에 넣는것
        String result;

        result = String.format("문자서식 : %s, %S", str1, str1);
        System.out.println(result); //문자서식 : Happy, HAPPY

        //Int
        int myInt = 10;
        result = String.format("정수 서식 : %d", myInt); //%05d -> 다섯자리로 해줘 => 00010 으로 출력
        System.out.println(result);

        float myFloat = 12.545678f;
        result = String.format("실수 서식 : %f, %.1f, %.2f, %.3f", myFloat, myFloat, myFloat, myFloat); //12.545678, 12.5, 12.55, 12.546
        System.out.println(result);
    }
}
