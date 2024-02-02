package quiz.day3_week3;

public class ChuncheonTicket2 {
    public static void main (String[] args) {
        /**
         * 시립박물관 오픈 기념으로 시청 근무자들에게 박물관 티켓 1112장 무료배포
         * 최대 몇명까지 나눠줄 수 있고, 그때 몇장의 티켓이 남는가
         * 각각 개인은 4장의 티켓을 가져감
         */

        int freeTicket = 1111;
        int result = freeTicket/4;
        System.out.println("티켓을 가져 갈 수 있는 근무자들 수는?");
        System.out.println(result);

        int result2 = freeTicket%4;
        System.out.println("티켓을 다 나눠주고 남은 티켓 수는?");
        System.out.println(result2);

    }
}
