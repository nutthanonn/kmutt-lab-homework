public class Bicycle {

    private String ownerName;
    private String tagNo;

    public Bicycle() {
        this.ownerName = "unknow";
        this.tagNo = "unknow";
    }
    
    public String getTagNo() {
        return tagNo;
    }

    public void setTagNo(String tagNo) {
        this.tagNo = tagNo;
    }


    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }
}
