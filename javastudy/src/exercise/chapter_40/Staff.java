package exercise.chapter_40;

public class Staff {
    //속성
    private int salesAmount;

    //행위
    public int helpPayment(Customer customer, int price) {
        return customer.calculatePrice(price); //돈을 얼마나 내는지 계산후 뱉어내도록
    }

//    public int helpPayment(VIPCustomer customer, int price) {
//        return customer.calculatePrice(price);
//    }

    public void addSalesAmount(int cash) {
        salesAmount += cash;
    }

    public void printMySalesAmount() {
        System.out.println("오늘의 최종 매상은 "+this.salesAmount+"원 입니다");
    }

    public void setSalesAmount(int salesAmount) {
        this.salesAmount = salesAmount;
    }
}
