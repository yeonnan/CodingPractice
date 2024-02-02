package exercise.chapter_27.pacakgeOne;

public class ClassA {
    //Public
    public String publicStr;

    //private
    private  String privateStr;

    //default
    String defaultStr;

    public void methodPublic(){};

    private void methodPrivate() {};

    void methodDefault(){};

    //자신 안에서 정의할때는 private 접근 가능
    void testPrivate() {
        String str = privateStr;
        methodPrivate();
    }

}
