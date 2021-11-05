prime-ejb-crud
===============

Aplicativo web demonstração, desenvolvido com Primefaces, EJB 3 e JPA. O Primefaces é uma extensão do JSF (JavaServer Faces), que disponibiliza uma série de componentes visuais pré-definidos. O componente EJB atua em conjunto com a JPA na camada servidor, os dados dessa aplicação são persistidos no banco de dados MySQL. O projeto implementa o estilo Web Profile da plataforma Java EE.

O objetivo dessa aplicação é servir como conteúdo no estudo de desenvolvimento de soluções para web, utilizando tecnologias produtivas com foco em qualidade e eficiência. A aplicação foi implantanda no Openshift, a plataforma de cloud computing (PaaS) da Red Hat.

Você pode acessar a aplicação no Openshift através da url: https://primefaces-yaw.rhcloud.com/

Detalhes da implementação
-------
Tecnologias utilizadas na implementação:
* Primefaces: extensão do JSF, disponibiliza uma série de componentes visuais iterativos. Sua proposta é acelerar o desenvolvimento Web, com foco em qualidade e eficiência em interfaces gráfica;
* JSF 2: utilizamos o framework JavaServer Faces, seguindo o modelo arquitetural MVC e o uso de componentes visuais para a construção das interfaces gráficas (front-end);
* EJB 3: a plataforma Java EE define uma série de componentes para o desenvolvimento de aplicações corporativas sofisticadas. Com EJBs é possível desenvolver aplicações distribuídas; integração/conectividade com legado; processamento assíncrono baseado Fila / Mensagens; controle transacional; e outros;
* JPA: API alto nível, padrão da tecnologia Java, para definir o mapeamento objeto relacional (ORM);
* Hibernate: provedor JPA, responsável por resolver ORM;
* Bean Validation: mecanismo padrão do Java para determinar regras de validação através de anotações;

Pré-requisitos
-------
* JDK - versão 1.6 do Java, ou mais recente;
* Eclipse - recomendamos o Eclipse IDE;
* Plugin para Eclipse - JBoss Tools;
* Maven - para build e dependências.
* Application Server Java EE - JBoss AS 6 ou 7 (EAP);
* MySQL - versão 5 ou mais recente;

Saiba mais
-------
Visite a página do projeto:
http://www.yaw.com.br/open/projetos/primefaces-ejb3/
