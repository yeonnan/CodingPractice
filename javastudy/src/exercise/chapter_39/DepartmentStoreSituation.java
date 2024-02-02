package exercise.chapter_39;

import exercise.chapter_34.Customer;
import exercise.chapter_34.GoldCustomer;
import exercise.chapter_34.Staff;
import exercise.chapter_34.VIPCustomer;

public class DepartmentStoreSituation {

    public static void main(String[] args) {

        //전제상황
        int price = 10_000;
        Staff staff = new Staff();
        staff.setSalesAmount(1_000_000);

        Customer customer = new VIPCustomer("이도"); //단골손님

        Customer[] customerQueue = {
                customer, new Customer("이산"), customer,
                new VIPCustomer("김좌진"), new Customer("안중근"), new VIPCustomer("안창호"),
                new Customer("윤봉길"), new Customer("김구"), customer,
                new GoldCustomer("이창섭"), new GoldCustomer("임현식"), new GoldCustomer("서은광")

        };

        //시나리오
        for (Customer customerEach : customerQueue) {
            customerEach.printMyInfo();
            int cash = staff.helpPayment(customerEach, price);
            System.out.printf("내가 내는 금액은 : %d\n", cash);
            staff.addSalesAmount(cash);

        }
        staff.printMySalesAmount();
    }
}
