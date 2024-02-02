package exercise.chapter_47;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SetInterfaceTest {
    public static void main(String[] args) {

        //set 인터페이스 구현
        Set<String> fruitSet = new HashSet<>();

        //add
        fruitSet.add("Orange");
        fruitSet.add("Apple");
        fruitSet.add("Mango");
        fruitSet.add("Grape");

        System.out.println("fruitSet : "+fruitSet);

        //add 중복 add
//        List<String> fruitList = new ArrayList<>();
//        fruitList.add("Orange");
//        fruitList.add("Apple");
//        fruitList.add("Mango");
//        fruitList.add("Grape");
//        fruitList.add("Apple");
//
//        System.out.println("fruitList : "+fruitList);

        //remove(set)
        fruitSet.remove("Apple");
        System.out.println("fruitSet : "+fruitSet);

        //contains
        System.out.println("Apple 있는지 : "+fruitSet.contains("Apple"));
        System.out.println("Mango 있는지 : "+fruitSet.contains("Mango"));

        //size, isEmpty, clear
        System.out.println("사이즈 : " + fruitSet.size());

        fruitSet.clear(); //비우기
        System.out.println("Set이 비었는지? : "+fruitSet.isEmpty());
        System.out.println("ftuitSet : "+fruitSet);
    }
}
