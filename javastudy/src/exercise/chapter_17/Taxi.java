package exercise.chapter_17;

public class Taxi {
    public static void main(String[] args) {

        //심야할증구간 : 0~4시
        //시외 할증 기준 : 서울 x, 서울 외각  o
        int goHomeTime = 3;
        String myHome = "기흥";
        int payment = 10_000;

        if (0 < goHomeTime && goHomeTime < 4) {
            payment = payment + (int) (payment*0.2); //10000->12000
        }
        if (myHome != "서울") {
            payment = payment + (int) (payment*0.2); //12000 + (12000*0.2) = 14400
        }
        String result = String.format("고객님이 내셔야할 돈은 %d 입니다", payment);
        System.out.println(result);
    }
}
