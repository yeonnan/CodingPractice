package org.example.base;

import org.example.Person.Person;
import org.example.Person.PersonDto;
import org.example.Person.PersonMapStruct;

//PersonDto->person으로 변환해라(필드이름이 다를 수 있다)

public class Main {
    public static void main(String[] args) {
        // PersonDto to Person
        PersonDto personDto = new PersonDto();
        personDto.setName("John Doe");
        personDto.setAge(30);
        personDto.setAddress("123 Street, City");
        personDto.setEmail("john.doe@example.com");
        personDto.setPhone("123-456-7890");
        personDto.setGender("Male");
        personDto.setNationality("American");
        personDto.setEducation("Bachelor's Degree2");

        System.out.println(personDto);

        Person person = new Person();
        person.setFullName(personDto.getName());
        person.setYears(personDto.getAge());
        System.out.println(person);

        Person person2 = PersonMapStruct.INSTANCE.personDtoToPerson(personDto);
        System.out.println("person2: "+person2);
    }
}
