package exercise.chapter_53;

public class OuterClass {

    private int outerData;

    public OuterClass(int outerData) {
        this.outerData = outerData;
    }

    public class InnerClass{

        private int innerDate;

        public InnerClass(int innerDate) {
            this.innerDate = innerDate;
        }
        void display() {
            System.out.println("OuterData : " +outerData);
            System.out.println("InnerData : " +innerDate);
        }
    }
}
