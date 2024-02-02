package exercise.chapter_44;

public class StringBuilderTest {

    public static void main(String[] args) {
        // +=
        String str = "";

        long startTime = System.currentTimeMillis();

        for (int i = 0; i < 50000; i++) {
            str += "cat";
        }
//        System.out.println(str);

        long endTime = System.currentTimeMillis();
        System.out.println("string 걸린시간 : "+(endTime - startTime)+ "ms");

        //////////

        long startTime2 = System.currentTimeMillis();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 50000; i ++) {
//            sb.append("cat");
        }

        String output = sb.toString();
        System.out.println(output);

        long endTime2 = System.currentTimeMillis();
        System.out.println("sb 걸린시간 : "+(endTime - startTime)+ "ms");

    }
}
