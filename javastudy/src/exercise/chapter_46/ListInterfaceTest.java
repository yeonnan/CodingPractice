package exercise.chapter_46;

import java.util.ArrayList;
import java.util.List;

public class ListInterfaceTest {
    public static void main(String[] args) {

        //List 정의
        List<String> fruitList = new ArrayList<>();

        //add
        fruitList.add("Orange");
        fruitList.add("Apple");
        fruitList.add("Banana");
        fruitList.add("Kiwi");

        System.out.println("FruitList 요소 : " + fruitList); //FruitList 요소 : [Orange, Apple, Banana, Kiwi]

        //add(index, element)
        fruitList.add(3, "Mango");
        System.out.println("FruitList 요소 : " + fruitList); //FruitList 요소 : [Orange, Apple, Banana, Mango, Kiwi]

        //remove(index)
        fruitList.remove(3);
        System.out.println("FruitList 요소 : " + fruitList); //FruitList 요소 : [Orange, Apple, Banana, Kiwi]

        //get(index)
        String myFruit = fruitList.get(3);
        System.out.println("가져온 과일은 : "+myFruit); //가져온 과일은 : Kiwi

        //set(index, element)
        fruitList.set(1, "PineAppel");
        System.out.println("FruitList 요소 : " + fruitList); //FruitList 요소 : [Orange, PineAppel, Banana, Kiwi]

        //size
        System.out.println("리스트 사이즈 : "+fruitList.size()); //리스트 사이즈 : 4

        //isEmpty : 현재 리스트가 비었는지 안비웠는지 확인
        List<String> fruitList2 = new ArrayList<>();
        System.out.println(fruitList2.isEmpty()); //true
        System.out.println(fruitList.isEmpty()); //false

        //contains : 리스트에 해당 원소가 있는지 없는지 확인하는 메서드
        System.out.println(fruitList.contains("Kiwi")); //true
        System.out.println(fruitList.contains("Apple")); //false

        //indexof, clear
        String myFruit2 = "Orange";
        System.out.println(fruitList.indexOf(myFruit2)); //0
        String myFruit3 = "Apple";
        System.out.println(fruitList.indexOf(myFruit3)); //-1, 아무것도 없으면 -1이 나옴

        fruitList.clear();
        System.out.println("FruitList 요소 : " +fruitList); //FruitList 요소 : []


    }
}
