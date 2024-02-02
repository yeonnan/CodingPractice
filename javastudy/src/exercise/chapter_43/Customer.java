package exercise.chapter_43;

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

    public Customer(String customerID, String name) {
        this(name); //아래 name 호출
        this.customerID = customerID; //customerID만 덮어서 오버라이딩
    }

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

    @Override
    public String toString() {
        return String.format("Customer(customerID:%s, name:%s, customerGrade=%s, bonusPoint=%s)\n",
                            this.customerID, this.name, this.customerGrade,this.bonusPoint);
    }

    @Override
    public boolean equals(Object obj) { //다른 object가 뒤에 오는데 그거랑 같은지 비교할거다
        if (obj == null) {
            return false;
        }
        if (obj instanceof Customer) { //다운캐스팅
            Customer customer = (Customer) obj;
            return customer.customerID == this.customerID;
        }
        return false;
    }
}
