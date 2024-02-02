package exercise.chapter_19;

public class OddNumberTotal {
    public static void main (String[] args) {

        int total = 0;

        for(int i = 1; i <= 10; i++) {
            if (i % 2 ==0) {
                continue; //짝수들은 여기서 걸려서 다시 위로 올라감
            }
            System.out.println(i); //홀수들만 추출
            total += i;
        }
        System.out.printf("0~10까지 홀수를 더한 값은 %d", total);
    }
}
