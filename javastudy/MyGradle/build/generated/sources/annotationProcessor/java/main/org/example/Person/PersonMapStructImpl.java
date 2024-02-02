package org.example.Person;

import javax.annotation.processing.Generated;

@Generated(
    value = "org.mapstruct.ap.MappingProcessor",
    date = "2023-10-31T19:03:10+0900",
    comments = "version: 1.5.3.Final, compiler: IncrementalProcessingEnvironment from gradle-language-java-8.2.jar, environment: Java 11.0.11 (AdoptOpenJDK)"
)
public class PersonMapStructImpl implements PersonMapStruct {

    @Override
    public Person personDtoToPerson(PersonDto personDto) {
        if ( personDto == null ) {
            return null;
        }

        Person person = new Person();

        person.setFullName( personDto.getName() );
        person.setYears( personDto.getAge() );

        return person;
    }
}
