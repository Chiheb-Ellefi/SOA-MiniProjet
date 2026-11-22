package tn.idl.campus;

import jakarta.jws.WebMethod;
import jakarta.jws.WebParam;
import jakarta.jws.WebService;
import java.util.List;

@WebService(
    serviceName = "ServiceCertifications",
    targetNamespace = "http://campus.idl.tn/certifications"
)
public class ServiceCertifications {

    // Données fictives conservées en mémoire
    private final List<Certification> catalogue = List.of(
        new Certification("PCEP", "Python Entry-Level Programmer", "programmation", "debutant", 30, 120.0),
        new Certification("AZ900", "Cloud Fundamentals", "cloud", "debutant", 24, 150.0),
        new Certification("CCNA", "Réseaux niveau associé", "reseaux", "intermediaire", 80, 300.0),
        new Certification("PSM1", "Scrum Master niveau 1", "agilite", "debutant", 16, 200.0)
    );

    /** Retourne toutes les certifications du catalogue. */
    @WebMethod
    public List<Certification> listerCertifications() {
        return catalogue;
    }

    /** Retourne une certification à partir de son code, ou lève une erreur métier. */
    @WebMethod
    public Certification consulterCertification(@WebParam(name = "code") String code)
            throws CertificationIntrouvableException {
        if (code == null || code.isBlank()) {
            throw new CertificationIntrouvableException("Le code est obligatoire.");
        }
        return catalogue.stream()
            .filter(c -> c.getCode().equalsIgnoreCase(code))
            .findFirst()
            .orElseThrow(() -> new CertificationIntrouvableException(
                "Certification introuvable : " + code));
    }

    /** Retourne les certifications d'un domaine (liste vide si aucune). */
    @WebMethod
    public List<Certification> rechercherParDomaine(@WebParam(name = "domaine") String domaine) {
        if (domaine == null || domaine.isBlank()) {
            return List.of();
        }
        return catalogue.stream()
            .filter(c -> c.getDomaine().equalsIgnoreCase(domaine))
            .toList();
    }

    /** Avancé : confirmation de réservation simulée. Le matricule n'est pas une authentification. */
    @WebMethod
    public String reserverPlaceSeminaire(@WebParam(name = "idSeminaire") int idSeminaire,
                                         @WebParam(name = "matricule") String matricule) {
        if (idSeminaire <= 0 || matricule == null || matricule.isBlank()) {
            return "Erreur : paramètres invalides.";
        }
        return "Réservation simulée confirmée pour " + matricule + " au séminaire " + idSeminaire;
    }
}
