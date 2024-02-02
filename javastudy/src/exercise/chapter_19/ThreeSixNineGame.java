package exercise.chapter_19;

public class ThreeSixNineGame {
    public static void main(String[] args) {

        for (int num = 1; num <= 30; num++) {

            if (num % 3 ==0) { //숫자가 들어왔을 때 3의 배수이면 짝을 치고 continue해라
                System.out.print("짝,");
                continue;
            }
            System.out.printf("%d,", num);
        }
    }
}
