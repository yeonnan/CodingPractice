package exercise.chapter_53;

public class LocalTest {
    public static void main(String[] args) {
        //로컬클래스
        class LocalWalk implements Walkable {

            @Override
            public void walk() {
                System.out.println("LocalWalk : walking");
            }
        }

        LocalWalk localWalk = new LocalWalk();
        localWalk.walk();

        int i = 100;

        //익명클래스
        Walkable anonymousWalk = new Walkable() {
            @Override
            public void walk() {
                System.out.println("i : "+i);
                System.out.println("anonymousWalk : Walking");
            }
        };
        anonymousWalk.walk();
    }
}
