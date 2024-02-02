package exercise.chapter_43;

public class EqualsTest {

    public static void main(String[] args) {
        Customer customer1 = new Customer("ID1", "민철"); //id를 외부에서 정해줌
        Customer customer2 = customer1;

        Customer customer3 = new Customer("ID1", "민철");
        Customer customer4 = new Customer("ID1", "철민");

        System.out.println(customer1); //Customer(customerID:ID1, name:민철, customerGrade=SILVER, bonusPoint=0)
        System.out.println(customer3); //Customer(customerID:ID1, name:민철, customerGrade=SILVER, bonusPoint=0)

        System.out.println(customer1.equals(customer2)); //true
        System.out.println(customer1.equals(customer3)); //true
        System.out.println(customer1.equals(customer4)); //true
    }
}
