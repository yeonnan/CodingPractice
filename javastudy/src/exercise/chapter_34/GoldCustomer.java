package exercise.chapter_34;

public class GoldCustomer extends Customer{

    private double discountRatio; //할인율

    //행위
    @Override
    public int calculatePrice(int price) {
        this.bonusPoint += price * bonusPointRatio;
        price -= price * discountRatio;
        return price;
    }

    public GoldCustomer(String name) {
        super();
        this.customerID = "Customer" + Customer.serialNums++; //요구사항에 고객  id는 cuostmer{숫자}로 순차생성
        this.name = name;
        this.customerGrade = "GOLD";
        this.bonusPoint = 0;
        this.discountRatio = 0.03;
        this.bonusPointRatio = 0.03;
    }
}
