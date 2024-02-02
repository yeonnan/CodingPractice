package exercise.chapter_24;

public class Scores {
    public static void main(String[] args) {

        //A class 학생들 점수
        int studentAClass1 = 50;
        int studentAClass2 = 30;
        int studentAClass3 = 45;

        //B class 학생들 점수
        int studentBClass1 = 60;
        int studentBClass2 = 65;
        int studentBClass3 = 66;

        //A class average
        double averageAClass = calculateAverage(studentAClass1,studentAClass2,studentAClass3);

        //B class average
        double averageBClass =calculateAverage(studentBClass1,studentBClass2,studentBClass3);

        System.out.printf("A 학급의 평균 점수는 %.2f, B 학급의 평균 점수는 %.2f\n",averageAClass, averageBClass);
    }

    //a class와 b class의 결과값이 같은 함수를 사용한다. calculateAverage를 이용하여 a,b average를 구함
    //다른점은 인자라고 부르는 파라미터가 다른것 ex. AClass1,AClass2,AClass3 BClass1,BClass2,BClass3
    //studentAClass1이 studentScore1로 바껴서 계산됨
    static double calculateAverage(int studentScore1, int studentScore2, int studentScore3) {
        int sumBClass = studentScore1+studentScore2+studentScore3;
        return sumBClass / (double)3;
    }
}
