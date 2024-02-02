package exercise.chapter_19;

public class StarTriangle {
    public static void main(String[] args) {

        int row;
        int colum;

        for (row = 1; row <= 9; row++) {
            for (colum = 1; colum <= row; colum++) {
                System.out.print('*');
            }
            System.out.println();
        }
    }
}
