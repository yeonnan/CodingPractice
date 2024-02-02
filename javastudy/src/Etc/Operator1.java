package Etc;

public class Operator1 {

    public static void main(String[] args) {
        //대입연산자
        int a = 10;
        int b = a;
        int c = b;
        System.out.println(c);

        //부호연산자
        int positive3 = 3;
        int negative3 = -3;
        System.out.println(positive3);
        System.out.println(negative3);

        //산술연산자 + - * / %
        int num1 = 10;
        int num2 = 5;
        int num3 = 30;
        int result = (num1 + num2) * num3;
        System.out.println(result);
    }
}
