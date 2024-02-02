package exercise.chapter_20;

public class ArrayFor {
    public static void main(String[] args) {

        int[] studentScores = {90, 87, 88, 75, 99, 65};

        //for loop
        for (int i = 0; i < studentScores.length; i++) { //array 초기값은 0, studentScores.length 스코어즈의 길이
            System.out.printf("이 array의 %d의 인덱스의 값은 %d 이다\n",i, studentScores[i]);
        }

        //for loop
        for (int score: studentScores) { //쭉 한바퀴 돌면서 순회 하는 것
            System.out.printf("student의 값은 %d이다 \n", score);
        }
    }
}