package exercise.chapter_31;

public class Fish {
    //속성
    private String gender; //"Male", "Female"
    protected boolean havingPoison; //true 독이 있고,  false 독이없고
    private String StartSpawningDate; //산란 시작 시각
    private String endSpawningDate; //산란 종료 시각
    private String leavingSea; //사는 속성

    //행위
    void eat(String food) {
        System.out.printf(myInfo() +" 는 %s를 먹고 있습니다 \n", food);
    }
    void swim(int meter) {
        System.out.println("나는 헤엄칩니다 미터 : " +meter);
    }
    void makeCrowd(Fish otherfish) {
        System.out.println("나는 다른 물고기와 무리짓습니다");
    }
    void sleep(){};

    String myInfo() {
        return String.format("물고기(gender=%s,havingPoison=%b,leavingSea=%s)\n",
                this.gender, this.havingPoison, this.leavingSea);
    }

    void printfMyInfo(){
        System.out.println(myInfo());
    }

    

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void setHavingPoison(boolean havingPoison) {
        this.havingPoison = havingPoison;
    }

    public void setStartSpawningDate(String startSpawningDate) {
        StartSpawningDate = startSpawningDate;
    }

    public void setEndSpawningDate(String endSpawningDate) {
        this.endSpawningDate = endSpawningDate;
    }

    public void setLeavingSea(String leavingSea) {
        this.leavingSea = leavingSea;
    }

    public boolean isHavingPoison() {
        return havingPoison;
    }
}
