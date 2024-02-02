package exercise.chapter_27.pacakgeTwo;

import exercise.chapter_27.pacakgeOne.ClassA;

public class ClassB {
    public void testPublic(ClassA classA) {
        String str = classA.publicStr;
        classA.methodPublic();
    }

    //불가능
//    public void testPrivate(ClassA classA) {
//        String str = classA.privateStr;
//        classA.methodPublic();
//    }

    //다른 패키지라서 불가능
//    public void testDefault(ClassA classA) {
//        String str = classA.defaultStr;
//        classA.methodDefault();
//    }
}
