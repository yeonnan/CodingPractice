package exercise.chapter_32.fish;

public class FishChild extends Fish {

    private boolean eatable;
    protected String leavingSeaChild;

    //새로운 메소드
    public void digging() {
        System.out.println(myInfo() + "가 모래를 파고있습니다");
    }

    public boolean isEatable() {
        return eatable;
    }

    public void setEatable(boolean eatable) {
        this.eatable = eatable;
    }

    public void becomeDanger() {
        this.havingPoison = true;
    }

    @Override
        //컴퓨터에게 부모 클래스에 있는건데 다시 수정할거야 라고 알려주는 것
    void eat(String food) {
        System.out.printf(myInfo() + " 는 %s를 아주 열심히먹고 있습니다 \n", food);
    }

    void printSea() {
        System.out.println(myInfo() + "는" + this.leavingSeaChild + "바다 출신이고," +
                "부모 물고기는 " + super.leavingSea + " 바다 출신이야");
    }

    public void setLeavingSeaChild(String leavingSeaChild) {
        this.leavingSeaChild = leavingSeaChild;
    }

    FishChild() {
        super(); //부모 물고기가 만들어지고 있습니다
    }

    public FishChild(boolean eatable, String leavingSeaChild) {
        this.eatable = eatable;
        super.leavingSea = leavingSeaChild;
    }

    public FishChild(String gender, boolean havingPoison, String startSpawningDate, String endSpawningDate, String leavingSea, boolean eatable) {
        super(gender, havingPoison, startSpawningDate, endSpawningDate, leavingSea);
        this.eatable = eatable;
    }

    FishChild(String gender, boolean eatable, String leavingSea) {
        super(gender, false, "2022", "2022", leavingSea);
        this.eatable = eatable;

    }
}