# from sqlalchemy import create_engine, Column, Float, Text, TIMESTAMP, func
# from sqlalchemy.dialects.postgresql import UUID, ARRAY
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import uuid
#
# DATABASE_URL = "postgresql://dev:Shreeji123%40@localhost:5432/resume_db"
#
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)
#
# Base = declarative_base()
#
# class Candidate(Base):
#     __tablename__ = "candidates"
#
#     id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
#     name = Column(Text, nullable=False)
#     email = Column(Text, nullable=False)
#     location = Column(Text)
#     job_role = Column(Text)
#     resume_path = Column(Text)
#     jd_path = Column(Text)
#     match_score = Column(Float)
#     matched_keywords = Column(ARRAY(Text))
#     feedback = Column(Text)
#     created_at = Column(TIMESTAMP, server_default=func.now())
#
# Base.metadata.create_all(bind=engine)
