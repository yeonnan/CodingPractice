package exercise.chapter_39;

import exercise.chapter_33.Animal;
import exercise.chapter_33.Bird;
import exercise.chapter_33.Person;

public class AnimalDownCasting {

    public static void main(String [] args) {
        //다운캐스팅 확인여부

        Animal animal = new Bird();
//        checkBirdAndFly(animal);
        Person person = (Person) animal;  //bird로 했으면 bird로만 가능 person불가능

//        Animal animal2 = new Animal();
//        checkBirdAndFly(animal2);
//
//        Animal animal3 = new Person();
//        checkBirdAndFly(animal3);

        animal = null;
        animal.sleep();

    }
    static void checkBirdAndFly(Animal animal) {
        if (animal instanceof Bird) {
            Bird bird = (Bird) animal;
            bird.fly();
        }
        else {
            System.out.println("너는 새가 아니야");
        }

    }
}
