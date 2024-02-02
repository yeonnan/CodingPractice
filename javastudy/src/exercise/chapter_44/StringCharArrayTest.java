package exercise.chapter_44;

public class StringCharArrayTest {

    public static void main(String[] args) {

        //CharArray -> String
        char[] chars = {'a', 'b', 'c'};

        // CharArrayfmf String으로 바꾸는 2가지 방법
        //1번째
        String str1 = new String(chars);
        //2번째
        String str2 = String.valueOf(chars);

        System.out.println(str1);
        System.out.println(str2);

        //String도 char로 바꿀 수 있다
        char[] chars2 = str1.toCharArray();
        for (char ch:chars2) {
            System.out.println(ch);
        }
        System.out.println(str1.charAt(0)); //첫번째 인덱스에 맞는 char값 출력
        System.out.println(str1.charAt(1));
        System.out.println(str1.charAt(2));
    }
}
