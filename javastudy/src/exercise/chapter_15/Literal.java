package exercise.chapter_15;

public class Literal {

    public static  void main(String[]args) {

        int num = 0b1010; //2진법 10
        System.out.println(num);

        int num2 = 0xAC0; //16진법   12 * 16 + 10 * 16^2 = 2752
        System.out.println(num2);

        double myDouble = 5.22E5; //E5라는 뜻은 10의 5제곱
        System.out.println(myDouble); //522000.0

        double myDouble2 = 2.55E-3;
        System.out.println(myDouble2); //0.00255

        //null
        String str = null;
        System.out.println(str); //null
    }
}
