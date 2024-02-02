package exercise.chapter_42;

public class Customer {
    //속성
    static int serialNums = 1;



    protected String customerID; //고객ID
    protected String name; //고객 이름
    protected String customerGrade; //고객 등급

    protected int bonusPoint; //보너스 포인트
    protected double bonusPointRatio; //포인트 적립 비율

    //행위
    public int calculatePrice(int price) {
        this.bonusPoint += price * bonusPointRatio; //스스로 포인트 적립
        return price;
    }

    Customer(){}

    //고객 생성 -> 생성자 만들기
    public Customer(String name) {
        this.customerID = "Customer" + serialNums++; //고객 ID는 순차생성
        this.name = name;
        this.customerGrade = "SILVER"; //실버 등급으로 시작
        this.bonusPointRatio = 0.01; //포인트 비율은 0.01포인트
        this.bonusPoint = 0; //보너스 포인트 처음 왔을때는 0
    }

    public void printMyInfo() {
        System.out.printf("Customer(customerID:%s, name:%s, customerGrade=%s, bonusPoint=%s)\n",
                this.customerID, this.name, this.customerGrade,this.bonusPoint );
    }
}
