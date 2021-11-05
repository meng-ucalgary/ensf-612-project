#simple-stax
simple xml parser based on StAX.
* You can easily parse the xml to object by Element unit.
* In addition, it is faster because the stream based parsing.
* It can parse to various types such as String, Integer, Boolean, Map, List ... and your specific Object.

## Getting Started
add dependency to your pom.xml
```xml
<dependency>
  <groupId>org.lima.parser</groupId>
  <artifactId>simple-stax</artifactId>
  <version>0.0.1</version>
</dependency>
```

## Example
* your/xml/file:
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<info>
  <version>1</version>
  <name>movie list</name>
</info>
<movie-list>
  <movie>
    <id>1234</id>
    <title>Iron Man 3</title>
    <credits>
      <credit>Robert Downey Jr.</credit>
      <credit>Gwyneth Paltrow</credit>
    </credits>
  </movie>
  <movie>
    <id>5678</id>
    <title>Thor: The Dark World</title>
    <credits>
      <credit>Chris Hemsworth</credit>
      <credit>Natalie Portman</credit>
      <credit>Tom Hiddleston</credit>
    </credits>
  </movie>
</movie-list>
```

* If you want to parse "info" element:
```java
class Info {
  public String id;
  public String title;
  public List<String> credits;
}
```
```java
import org.lima.parser.sstax.XMLParser;

class Main {
  public static void main(String[] args) throws Exception {
    XMLParser parser = new XMLParser(new FileInputStream(new File("your/xml/file")));
    
    Info info = parser.parseObject("info", Info.class);
    
  }
}
```

* If you want to parse "movie-list" element:
```java
class Movie {
  public Iteger version;
  public String name;
}
```
```java
import org.lima.parser.sstax.XMLParser;

class Main {
  public static void main(String[] args) throws Exception {
    XMLParser parser = new XMLParser(new FileInputStream(new File("your/xml/file")));
    
    // if you want to parse all of list,
    List<Movie> movieList = parser.parseList("movie-list", Movie.class);
    
    // if you want to parse iterable (for large size xml),
    Iterator<Movie> movieIterator = parser.getListIterator("movie-list", Movie.class);
    while(movieIterator.hasNext()) {
      Movie movie = movieIterator.next();
    }
  }
}
```
