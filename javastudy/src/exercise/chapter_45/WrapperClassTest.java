package exercise.chapter_45;

public class WrapperClassTest {

    public static void main(String[] args) {

        //Integer
        Integer integer1 = new Integer(20); //int -> integer boxing
        Integer integer2 = new Integer(30);

        int int1 = integer1.intValue(); //unboxing, integer -> int 바꾼것

        Integer integer3 = 20;  //autoboxing, new integer(20);
        int int2 = integer3; //autoboxing

        System.out.println(integer1);
        System.out.println(int1);
        System.out.println(integer3);
        System.out.println(int2);

        //연산자
        System.out.println(integer1 + integer2);
        System.out.println(integer1 + int1);

        //character
        Character character = new Character('X'); //'X' charType -> Character boxing
        char ch1 = character.charValue(); //character -> char unboxing

        Character character1 = 'x';
        char ch2 = character1;

        System.out.println(character);
        System.out.println(ch1);

        Character[] characters = {'a', 'b', 'c'};
        char[] chars = {'a', 'b', 'c'};

        String str = String.valueOf(characters); //[Ljava.lang.Character;@5594a1b5
        String str2 = String.valueOf(chars); //abc

        System.out.println(str);
        System.out.println(str2);

        //Booelan Type
        Boolean boolean1 = new Boolean(true); //true boolean -> Boolean
        boolean b1 = boolean1.booleanValue(); //unboxing

        Boolean boolean2 = false;
        boolean b2 = boolean2;

        System.out.println(boolean1 & boolean2); //false
        System.out.println(boolean1 | boolean2); //true

    }
}
