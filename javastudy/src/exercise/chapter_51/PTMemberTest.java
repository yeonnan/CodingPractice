package exercise.chapter_51;

public class PTMemberTest {
    public static void main(String[] args) {
        PTMember member = new PTMember("민철", 178, 70, "Male");

        member.setID("abcd");
        System.out.println(member);
    }
}

