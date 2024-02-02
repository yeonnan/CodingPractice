package exercise.chapter_30;

import exercise.chapter_28.Teacher;

public class Student {
    static int serialNum = 1;
    static String city = "Seoul";

    //속성
    private String schoolName;
    private int classYear; //몇학년
    private int classroomNumbers; //몇반
    private int studentNumber; //몇번

    private int studentID; //student 고유 ID

    //기본정보
    private String name;
    private String gender;

    //정적 메소드
    public static int getSerialNum() {
        return serialNum;
    }
    public static void setSerialNum(int num) {
        serialNum = num;
    }

    //행위
    void study(Teacher teacher, String subjectName) {
        String teacherName = teacher.getName();
        System.out.printf("학생 : 저는 %s 선생님께 %s 과목을 배웁니다 \n", teacherName, subjectName);
    }

    public void printMyInfo() {
        System.out.printf("[Student] schoolName : %s, classYear : %d, classroomNumbers : %d" +
                "classroomNumbers : %d, studentID : %d, name : %s, gender : %s\n",
                this.schoolName, this.classYear, this.classroomNumbers,
                this.studentNumber, this.studentID, this.name, this.gender);
    }


    //생성자
    Student() {
    }
    Student(String name, String gender) {
        this("School", 1, 3, -1,name, gender);
    }

    //파라미터
    //생성자를 만들게 되면 생성자에 들어가는 함수가 자동으로 매칭이 되도록 만드는 중
    Student(String schoolName, int classYear, int classroomNum, int studentNum, String name, String gender) {
        this.studentID = serialNum++;
        this.schoolName = schoolName;
        this.classYear = classYear;
        this.classroomNumbers = classroomNum;
        this.studentNumber = studentNum;
        this.name = name;
        this.gender = gender;
    }

    //getter
    public String getName() {
        return this.name;
    }
}
