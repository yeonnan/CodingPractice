package quiz.day3_week3;

public class ChuncheonTicket3 {
    public static void main(String[] args) {
        /**
         * 서로 다른 3명의 손님이 왔다. 3명은 반값 할인 적용 대상인가 아닌가
         * 나이가 65세 이상이고, 국적이 한국이면 반값으로 줄 예정이다
         * Alice(나이: 70, 나라: 미국)
         * Kim (나이: 65, 나라: 한국)
         * Yoo (나이: 42, 나라: 한국)
         */

        final int SENIOR_AGE_STANDRAD = 65;

        int ageAlice = 70;
        String countryAlice = "USA";

        int ageKim = 65;
        String countryKim = "KOR";

        int ageYoo = 42;
        String countryYoo = "KOR";

        boolean Alice = (ageAlice >= SENIOR_AGE_STANDRAD) && (countryAlice == "KOR");
        boolean Kim = (ageKim >= SENIOR_AGE_STANDRAD) && (countryKim == "KOR");
        boolean Yoo = (ageYoo >= SENIOR_AGE_STANDRAD) && (countryYoo == "KOR");

        System.out.println("Alice는 적용 대상자인가?");
        System.out.println(Alice);

        System.out.println("Kim은 적용 대상자인가?");
        System.out.println(Kim);

        System.out.println("YOO는 적용 대상자인가?");
        System.out.println(Yoo);
    }
}
