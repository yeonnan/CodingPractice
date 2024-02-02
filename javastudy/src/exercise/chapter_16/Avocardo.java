package exercise.chapter_16;

public class Avocardo {

    public static void main(String[] args) {
//        //장보기 전
//        int milks = 0; //우유 0개
//        int avocados = 0; //아보카도 0개
//        boolean existedAvocado = true; //아보카도가 있는가 true
//
//        //장보기
//        milks = (existedAvocado) ? 6:0;
////        if(existedAvocado) {
////            milks = 6;
////        } else {
////            milks = 1;
////        }
//
//        //집으로 돌아오기
//        String comment = String.format("장보고 돌아왔어 %d개 아보카도, %d개 우유", avocados, milks);
//        System.out.println(comment);

        //장보기 전
        int Milks = 0; //우유 0개
        int avocados = 0; //아보카도 0개
        boolean existedAvocado = true; //아보카도가 있는가 true

        //장보기
        int milks = 1;
        if(existedAvocado) {
            avocados = avocados+6;
        }

        //집으로 돌아오기
        String comment = String.format("장보고 돌아왔어 %d개 아보카도, %d개 우유", avocados, milks);
        System.out.println(comment); //아보카도 6개, 우유 1개
    }

}


