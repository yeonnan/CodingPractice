package exercise.chapter_56;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;

public class FileWriterTest {
    public static void main(String[] args) {

        String content = "이것은 파일 컨텐츠 입니다";

        //기존 파일은 그대로 있고 뒤에 이어붙이기 하고 싶을 땐 true 붙이기
        try (FileWriter fos = new FileWriter("HelloWorld/src/exercise/chapter_56/output_korean.txt" )){
            fos.write(content);

            System.out.println("txt파일이 생성되었습니다");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
