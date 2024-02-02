package exercise.chapter_28;

public class Person {

    private String name;
    private String gender;
    private int age;

    public void showMyself() {
        System.out.printf("Person 인스턴스: name:%s, gender:%s, age:%d\n",this.name, this.gender, this.age);
    }

    //파라미터가 더 많은 값을 호출하도록 하는것
    public Person(String name) {
        this(name, "unknown");
    }

    public Person(String name, String gender) {
        this(name, gender, -1);
    }

    public Person(String name, String gender, int age) {
        this.name = name;
        this.gender = gender;
        this.age = age;
    }

    //
    public Person returnMySelf() {
        return this; //나 자신 인스턴스 자체를 보냄
    }

}
