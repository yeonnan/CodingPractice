package exercise.chapter_52;

import java.util.Arrays;

public class DayEnumTest {
    public static void main(String[] args) {
        //각각 Enum값 정의
        //ordinal, compareTo, values

        Day monday = Day.MONDAY;
        Day sunday = Day.SUNDAY;
        Day thursday = Day.THURSDAY;

        System.out.println("ordinal 값 : "+monday.ordinal());
        System.out.println("ordinal 값 : "+sunday.ordinal());
        System.out.println("ordinal 값 : "+thursday.ordinal());

        System.out.println("compareto : "+monday.compareTo(sunday)); //1-0 = -1
        System.out.println("compareto : "+monday.compareTo(thursday)); //1-4 = -3

        Day[] days = Day.values();
        System.out.println("Days : " + Arrays.toString(days));
    }
}
