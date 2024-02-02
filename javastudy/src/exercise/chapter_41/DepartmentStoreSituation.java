package exercise.chapter_41;

public class DepartmentStoreSituation {

    public static void main(String[] args) throws InterruptedException {

        //전제상황
        int price = 10_000;
        Staff staff = new Staff();
        staff.setSalesAmount(1_000_000);

        String hello = "Hello";
        String hello1 = new String("Hello");
        String hello2 = new String("Hello");
        String hello3 = new String("Hello");

        Customer customer1 = new Customer("권율");
        Customer customer2 = new Customer("이순신");

        Customer customer3 = new VIPCustomer("이도");
        Customer customer4 = new VIPCustomer("아이유");
        Customer customer5 = new VIPCustomer("김혜수");
        Customer customer6 = new GoldCustomer("정우성");
        Customer customer7 = new GoldCustomer("손흥민");

        Customer[] customerQueue = {
                new GoldCustomer("이창섭")

        };

        //시나리오
        for (Customer customerEach : customerQueue) {
           customerEach.printMyInfo();
            int cash = staff.helpPayment(customerEach, price);
            System.out.printf("내가 내는 금액은 : %d\n", cash);
            staff.addSalesAmount(cash);

        }
        staff.printMySalesAmount();

        while (true){ //위에 프로그램이 끝나는거 방지
            Thread.sleep(100);
        }
    }
}
