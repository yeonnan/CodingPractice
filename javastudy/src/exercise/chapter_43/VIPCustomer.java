package exercise.chapter_43;

public class VIPCustomer extends Customer {
    static int serialNums = 1;


    //속성
    private String agentID; //vip 담당 직원 ID
    private double discountRatio; //구매 할인율

    //행위
    @Override
    public int calculatePrice(int price) {
        this.bonusPoint += price * bonusPointRatio; //적립
        price -= price * discountRatio; //구매 할인
        return price;
    }

    public void callAgent() {
        System.out.println("담당직원" + this.agentID + "님 문의 드릴게 있습니다");
    }

    public VIPCustomer (String name) {
        super();
        this.customerID = "VIP"+serialNums; //고객ID는 VIP{숫자}로 생성
        this.name = name;
        this.customerGrade = "VIP"; //VIP 등급으로 시작
        this.bonusPoint = 0;
        this.bonusPointRatio = 0.05; //포인트 비율
        this.discountRatio = 0.1;
    }

    public void setAgentID(String agentID) {
        this.agentID = agentID;
    }

    @Override
    public void printMyInfo() {
        System.out.print("VIP");
        super.printMyInfo();
         }

    @Override
    public String toString() {
        return "VIPCustomer{" +
                "agentID='" + agentID + '\'' +
                ", customerID='" + customerID + '\'' +
                ", name='" + name + '\'' +
                ", customerGrade='" + customerGrade + '\'' +
                ", bonusPoint=" + bonusPoint +
                '}';
    }
}

