package exercise.chapter_24;

public class MethodExamples {

    //일반적인 입력값, 출력값도 있는 경우
    //둘 다 하나인 경우

    //하나의 파라미터, 인트를 반환하는 함수 정의
    static int toUnicode(char ch) {
        return (int) ch;
    }

    //여러개의 파라미터, 어떤 값 두개를 더하고 곱하기 4 하는거
    static int sumAndMultiplyFour(int a, int b) {
        return (a + b) * 4;
    }

    public static void main(String[] args) {
        char ch = 'A';
        int decode = toUnicode(ch);
        System.out.println(decode);

        int myInt1 = 10;
        int myInt2 = 5;
        int result = sumAndMultiplyFour(myInt1, myInt2);
        System.out.println(result);

        //인자값이 없는데 출력값이 있어서 res에 넣고 실행
        String res = sayHello();
        System.out.println(res);

        //인자값이 있지만 출력값이 없는거
        printHello("printHello");
        //출력, 인자값 없는것
        printHi();
    }

    //인자값이 없을 수 있다, 출력값은 있음
    static String sayHello() {
        return "Hello";
    }

    //인자값이 있는데, 출력값은 없는거
    static void printHello(String str) {
        System.out.printf("함수 안에서 실행합니다. %s\n",str);
    }

    //인자값도 없고, 출력값도 없는거
    static void printHi() {
        System.out.println("Hi");
    }
}
