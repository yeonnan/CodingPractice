package exercise.chapter_27.pacakgeOne;

public class ClassAA {

    void testPublic(ClassA classA) {
        String str = classA.publicStr;
        classA.methodPublic();
    }

    //불가능
//    void testPrivate(ClassA classA) {
//        String str = classA.privateStr; //필드가 private 되어있어서 접근 불가
//        classA.methodPublic();
//    }

    //default는 같은 패키지 내에서는 사용 가능
    void testDefault (ClassA classA) {
        String str = classA.defaultStr;
        classA.methodDefault();
    }


}
