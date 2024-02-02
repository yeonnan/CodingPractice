package exercise.chapter_31;

public class FishChild extends Fish{

    private boolean eatable;

    //새로운 메소드
    public void digging() {
        System.out.println(myInfo()+"가 모래를 파고있습니다");
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

    @Override  //컴퓨터에게 부모 클래스에 있는건데 다시 수정할거야 라고 알려주는 것
    void eat(String food) {
        System.out.printf(myInfo() +" 는 %s를 아주 열심히먹고 있습니다 \n", food);
    }
}
