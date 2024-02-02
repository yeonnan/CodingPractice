package exercise.chapter_36;

import java.nio.file.WatchKey;

public class InterfaceTest {

    public static void main(String[] args) {
        //속성
        System.out.println(Flyable.atmosphereLimit);
//        Flyable.atmosphereLimit = 100;

        //Flyable
        Flyable bird = new Bird();
        Flyable airplane = new Airplane("AB1112");

        bird.fly();
        airplane.fly();

        //Walkable
        Walkable person = new Person();
        Person person2 = new Person();
        person2.setName("인텔리제이");

        Walkable robot = new Robot("RB1233");

        person.walk();
        robot.walk();

        if (robot instanceof Robot) {
            Robot robot2 = (Robot) robot; //다운캐스팅, 위에 walkable의 robot을 들고 온다는 의미로
            robot2.helpPerson(person2);
        }
    }
}
