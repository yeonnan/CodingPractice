package quiz.day3_week3;

public class ChuncheonTicket1 {
    public static void main (String[] args) {

        /**
         * 티켓값은 얼마인가?
         * 전문가 4명이 제시하는 적정 티켓 값의 평균값
         * kim 3000, park 5000, lee 2000, hong 2000
         */
        int kim = 3000;
        int park = 5000;
        int lee = 2000;
        int hong = 2000;

        int result = (kim+park+lee+hong) / 4;
        System.out.println(result); //3000
    }
}
